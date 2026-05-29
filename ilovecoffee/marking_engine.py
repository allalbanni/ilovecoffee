"""
Marking Engine Module - Handles answer comparison and marking logic
"""

import json
import re
from difflib import SequenceMatcher
from typing import Dict, List, Any


class MarkingEngine:
    """Handles automatic marking and answer comparison"""
    
    def __init__(self, threshold=0.8, ignore_case=True, mode='strict'):
        """
        Initialize marking engine
        
        Args:
            threshold: Similarity threshold (0-1) for flexible matching
            ignore_case: Whether to ignore case when comparing
            mode: Marking mode ('strict', 'flexible', 'keyword')
        """
        self.threshold = threshold
        self.ignore_case = ignore_case
        self.mode = mode.lower()
    
    def mark_answers(self, student_text, markscheme) -> Dict[str, Any]:
        """
        Compare student answers with markscheme
        
        Args:
            student_text: Extracted text from student PDF
            markscheme: Markscheme content (dict, list, or string)
            
        Returns:
            Dictionary with marking results
        """
        try:
            # Parse markscheme into structured format
            expected_answers = self._parse_markscheme(markscheme)
            
            # Extract student answers from text
            student_answers = self._extract_answers_from_text(student_text)
            
            # Match and mark
            results = self._match_and_mark(student_answers, expected_answers)
            
            return results
        
        except Exception as e:
            raise Exception(f"Error during marking: {str(e)}")
    
    def _parse_markscheme(self, markscheme) -> Dict[str, str]:
        """
        Parse markscheme into structured format
        
        Args:
            markscheme: Raw markscheme content
            
        Returns:
            Dictionary with question numbers as keys and expected answers as values
        """
        expected_answers = {}
        
        # If it's already a dict (from JSON), use it directly
        if isinstance(markscheme, dict):
            return markscheme
        
        # If it's a string, try to parse it
        if isinstance(markscheme, str):
            # Try JSON parsing first
            try:
                parsed = json.loads(markscheme)
                if isinstance(parsed, dict):
                    return parsed
            except json.JSONDecodeError:
                pass
            
            # Parse text format: "Q1: answer\nQ2: answer..." or "1. answer\n2. answer..."
            lines = markscheme.split('\n')
            question_num = 0
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                # Match patterns like "Q1:", "1.", "Question 1:", etc.
                match = re.match(r'^(?:Q|Question)?\s*(\d+)[\.:]\s*(.*)', line, re.IGNORECASE)
                
                if match:
                    question_num = int(match.group(1))
                    answer = match.group(2).strip()
                    expected_answers[str(question_num)] = answer
                elif question_num > 0 and line:
                    # Continuation of previous answer
                    expected_answers[str(question_num)] += " " + line
            
        return expected_answers if expected_answers else {"1": str(markscheme)}
    
    def _extract_answers_from_text(self, text) -> Dict[str, str]:
        """
        Extract student answers from OCR text
        
        Args:
            text: OCR extracted text from student PDF
            
        Returns:
            Dictionary with question numbers and student answers
        """
        student_answers = {}
        lines = text.split('\n')
        question_num = 0
        current_answer = ""
        
        for line in lines:
            line = line.strip()
            
            # Skip empty lines and page markers
            if not line or line.startswith('---'):
                if question_num > 0 and current_answer:
                    student_answers[str(question_num)] = current_answer.strip()
                    current_answer = ""
                continue
            
            # Match question patterns
            match = re.match(r'^(?:Q|Question)?\s*(\d+)[\.:]\s*(.*)', line, re.IGNORECASE)
            
            if match:
                if question_num > 0 and current_answer:
                    student_answers[str(question_num)] = current_answer.strip()
                
                question_num = int(match.group(1))
                current_answer = match.group(2)
            elif question_num > 0:
                current_answer += " " + line
        
        # Add last answer
        if question_num > 0 and current_answer:
            student_answers[str(question_num)] = current_answer.strip()
        
        return student_answers if student_answers else {"1": text}
    
    def _match_and_mark(self, student_answers: Dict[str, str], 
                       expected_answers: Dict[str, str]) -> Dict[str, Any]:
        """
        Match student answers with expected answers and mark
        
        Args:
            student_answers: Student's answers
            expected_answers: Expected answers from markscheme
            
        Returns:
            Marking results dictionary
        """
        results = {
            "total_questions": len(expected_answers),
            "correct_answers": 0,
            "questions": []
        }
        
        for q_num, expected_answer in expected_answers.items():
            student_answer = student_answers.get(q_num, "")
            
            # Compare answers based on mode
            if self.mode == 'strict':
                is_correct = self._strict_match(student_answer, expected_answer)
                similarity = 1.0 if is_correct else 0.0
            elif self.mode == 'flexible':
                similarity = self._calculate_similarity(student_answer, expected_answer)
                is_correct = similarity >= self.threshold
            else:  # keyword mode
                is_correct = self._keyword_match(student_answer, expected_answer)
                similarity = 1.0 if is_correct else 0.5
            
            # Generate feedback
            feedback = self._generate_feedback(
                student_answer, 
                expected_answer, 
                is_correct, 
                similarity
            )
            
            question_result = {
                "question_num": q_num,
                "student_answer": student_answer if student_answer else "No answer provided",
                "expected_answer": expected_answer,
                "status": "correct" if is_correct else "incorrect",
                "similarity": similarity,
                "feedback": feedback
            }
            
            results["questions"].append(question_result)
            
            if is_correct:
                results["correct_answers"] += 1
        
        # Calculate score percentage
        total = results["total_questions"]
        correct = results["correct_answers"]
        results["score_percentage"] = (correct / total * 100) if total > 0 else 0
        
        return results
    
    def _strict_match(self, student_answer: str, expected_answer: str) -> bool:
        """Check for exact match (with case handling)"""
        if self.ignore_case:
            return student_answer.lower().strip() == expected_answer.lower().strip()
        return student_answer.strip() == expected_answer.strip()
    
    def _calculate_similarity(self, student_answer: str, expected_answer: str) -> float:
        """Calculate similarity score using sequence matching"""
        s1 = student_answer.lower() if self.ignore_case else student_answer
        s2 = expected_answer.lower() if self.ignore_case else expected_answer
        
        matcher = SequenceMatcher(None, s1.strip(), s2.strip())
        return matcher.ratio()
    
    def _keyword_match(self, student_answer: str, expected_answer: str) -> bool:
        """Check if key terms from expected answer are present in student answer"""
        # Extract key terms (words longer than 3 characters)
        expected_words = set(
            word.lower() for word in re.findall(r'\b\w{4,}\b', expected_answer)
        )
        student_words = set(
            word.lower() for word in re.findall(r'\b\w{4,}\b', student_answer)
        )
        
        if not expected_words:
            return self._strict_match(student_answer, expected_answer)
        
        # At least 70% of key terms should be present
        matches = len(expected_words & student_words)
        return matches / len(expected_words) >= 0.7
    
    def _generate_feedback(self, student_answer: str, expected_answer: str, 
                          is_correct: bool, similarity: float) -> str:
        """Generate feedback message"""
        if is_correct:
            return "✓ Correct! Your answer matches the expected answer."
        
        if not student_answer:
            return "✗ No answer provided. Expected: " + expected_answer[:100]
        
        if self.mode == 'flexible':
            if similarity > 0.6:
                return f"⚠ Partially correct (Similarity: {similarity*100:.0f}%). Expected: {expected_answer[:80]}"
            else:
                return f"✗ Incorrect. Your answer doesn't match the expected answer. Expected: {expected_answer[:80]}"
        
        return f"✗ Incorrect. Expected: {expected_answer[:100]}"
