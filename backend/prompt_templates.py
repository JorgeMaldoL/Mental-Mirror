from ai_service import AIService

class JournalAI:
    def __init__(self):
        self.ai_service = AIService()
    
    def analyze_entry(self, journal_text):
        prompt = f"""
        You are a thoughtful journal analysis assistant. Analyze the following journal entry and provide:
        
        1. 2-3 thoughtful clarifying questions that help the person reflect deeper
        2. Gentle, supportive advice based on what was written
        3. Emotional reflection and validation of their feelings. 1-2 sentince long
        4. Assessment of whether this idea/thought seems well-developed or needs more exploration. 1-2 sentince long
        
        Please respond in a warm, empathetic tone as if you're a trusted friend.
        
        At the end, provide a completion assessment:
        - If the entry shows deep reflection and clear thinking: "✅ **Well Explored**: Your thinking on this seems thorough and well-developed!"
        - If the entry could benefit from more exploration: "🤔 **Keep Exploring**: This idea has more layers to uncover - consider reflecting further."
        - If the entry is just a daily update: "📝 **Good Check-in**: Nice to capture your day - feel free to dive deeper on anything specific."
        
        Journal Entry: {journal_text}
        
        Format your response with clear sections:
        **Clarifying Questions:**
        **Advice:**
        **Emotional Reflection:**
        **Completion Status:**
        """
        return self.ai_service.get_response(prompt, max_tokens=700)


class FeynmanAI:
    def __init__(self):
        self.ai_service = AIService()
    
    def evaluate_explanation(self, topic, explanation):
        prompt = f"""
        You are an expert educator using the Feynman Technique. Evaluate this student's explanation:
        
        Topic: {topic}
        Student's Explanation: {explanation}
        
        Please provide:
        1. What they explained well (positive reinforcement)
        2. Knowledge gaps or unclear areas that need work
        3. Specific suggestions for improvement
        4. Follow-up questions to test deeper understanding
        
        Be encouraging but constructive. Help them identify exactly where to focus their learning.
        
        Format your response with clear sections:
        **What You Did Well:**
        **Areas to Improve:**
        **Suggestions:**
        **Test Your Understanding:**
        """
        return self.ai_service.get_response(prompt, max_tokens=700)


class SummaryAI:
    def __init__(self):
        self.ai_service = AIService()
    
    def evaluate_summary(self, original_text, user_summary, summary_type, audience):
        prompt = f"""
        You are a writing coach evaluating a summary. Here's what you need to assess:
        
        Original Text: {original_text}
        User's Summary: {user_summary}
        Summary Type: {summary_type}
        Target Audience: {audience}
        
        Evaluate the summary on:
        1. Completeness - Did they capture the main ideas?
        2. Accuracy - Is the information correct?
        3. Conciseness - Is it appropriately brief?
        4. Clarity - Is it easy to understand for the target audience?
        5. Organization - Is the information well-structured?
        
        Provide specific, actionable feedback for improvement.
        
        Format your response:
        **Overall Assessment:**
        **Strengths:**
        **Areas for Improvement:**
        **Specific Suggestions:**
        **Score (1-10):**
        """
        return self.ai_service.get_response(prompt, max_tokens=600)