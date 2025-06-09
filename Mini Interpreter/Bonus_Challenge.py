def mini_interpreter(lines):
    vars = {}
    for line in lines:
        if line.startswith("let "):
            var, expr = line[4:].split("=")
            vars[var.strip()] = eval(expr, {}, vars)
        elif line.startswith("if "):
            cond, rest = line[3:].split(" then ")
            t_expr, f_expr = rest.split(" else ")
            print(eval(t_expr, {}, vars) if eval(cond, {}, vars) else eval(f_expr, {}, vars))
lines = [
    "let x = 5",
    "let y = x + 3",
    "if x > 3 then y else x"
]

mini_interpreter(lines)
