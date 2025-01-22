# custom-signals

### Signal Emit
  Emit is function, you can enter how much parameter want to get when its emit 
  ``` signal.emit(value) ```

### Signal Connect
  Connect is function and its parameter is a function. Which fucntion want you to run when its emits        
  ``` signal.connect(run) ```


## Example Code
```
# Import the Custom Signal
from custom_signals import CustomSignal


# function that will run when its emit
def run(user_name, user_id, message) -> None:
	print(f'User is {user_name}:{user_id} -> {message}!')

# Signal Object
singal = CustomSignal()

# Connect the function want to run 
singal.connect(run)

name = input("Enter Name :")
while True:
	id = 3
	message = input(f"{name}:")

	if not name == "":
		# Emit that will run the connected function
		singal.emit(name, id, message)



```
