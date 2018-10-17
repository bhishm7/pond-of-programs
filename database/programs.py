try:
    from program import AbstractProgram
except:
    from database.program import AbstractProgram
    
class SquareProgram(AbstractProgram):
    PROGRAM_NAME = 'Square'
    N_INPUTS = [int]
    N_OUTPUTS = [int]
    
    def execute(self, *args, **kwargs):
        # Returns the square of the passed number
        number = args[0]
        
        return number**2

class student(AbstractProgram):
	PROGRAM_NAME = "student"
	N_INPUTS=[int, int]
	N_OUTPUT=[int]

	def execute(self,*args):
		rollnum=args[0] 
		marks=args[1]
		return marks 
	
