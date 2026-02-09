from pyscript import display, document

def Username(e):
    document.getElementById("output").innerHTML = ""
    name = document.getElementById("user").value
    password = document.getElementById("pass").value

    if len(name) < 7:
        display("Username must be at least 7 characters", target="output")
    elif password.isalpha():
        display("Password must contain at least one number", target="output")
    elif password.isdigit():
        display("Password must contain at least one letter", target="output")
    elif len(password) < 10:
        display("Password must be at least 10 characters", target="output")
    else:
        display("Account created", target="output")