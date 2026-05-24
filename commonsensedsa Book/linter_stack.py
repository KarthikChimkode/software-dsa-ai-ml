class Linter:
    def __init__(self):
        self.stack = []
        self.error = None

    def lint(self, text):
        self.stack = [] # reset stack for each lint call
        self.error = None

        for index, char in enumerate(text):
            if self.is_opening_brace(char):
                self.stack.append(char)
            elif self.is_closing_brace(char):
                if self.closes_most_recent_opening_brace(char):
                    self.stack.pop()
                else:
                    self.error = f"Incorrect closing brace: {char} at index {index}"
                    return 
                

    def is_opening_brace(self, char):
        return char in "([{"
    
    def is_closing_brace(self, char):
        return char in ")]}"
    
    def opening_brace_of(self, char):
        return {')': '(', ']': '[', '}':'{' }.get(char)
    
    def most_recent_opening_brace(self):
        return self.stack[-1] if self.stack else None
    
    def closes_most_recent_opening_brace(self, char):
        return self.opening_brace_of(char) == self.most_recent_opening_brace