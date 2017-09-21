clear all;
syms x;
f=exp(2*x)*cos(3*x)
fd=diff(f)
ea_x=(10^-4)*(f/fd)

fprintf('%0.8e = f(3.14159265),(9d)\n', double(subs(f,x,3.14159265)));
fprintf('%0.8e = f(3.1415926),(8d)\n', double(subs(f,x,3.1415926)));
fprintf('%0.8e = f(3.141592),(7)\n', double(subs(f,x,3.141592)));
fprintf('%0.8e = f(3.14159),(6)\n', double(subs(f,x,3.14159)));
fprintf('%0.8e = f(3.1415),(5)\n', double(subs(f,x,3.1415)));
fprintf('%0.8e = f(3.141),(4)\n', double(subs(f,x,3.141)));
fprintf('%0.8e = f(3.14),(3)\n', double(subs(f,x,3.14)));
fprintf('%0.8e = f(3.1),(2)\n', double(subs(f,x,3.1)));
fprintf('%0.8e = ea_x(3.14159265)\n\n',double(subs(ea_x,x,3.14159265)));

fprintf('%0.8e = f(2.74683993),(9d)\n', double(subs(f,x,2.74683993)));
fprintf('%0.8e = f(2.7468399),(8d)\n', double(subs(f,x,2.7468399)));
fprintf('%0.8e = f(2.746839),(7)\n', double(subs(f,x,2.746839)));
fprintf('%0.8e = f(2.74683),(6)\n', double(subs(f,x,2.74683)));
fprintf('%0.8e = f(2.7468),(5)\n', double(subs(f,x,2.7468)));
fprintf('%0.8e = f(2.746),(4)\n', double(subs(f,x,2.746)));
fprintf('%0.8e = f(2.74),(3)\n', double(subs(f,x,2.74)));
fprintf('%0.8e = f(2.7),(2)\n', double(subs(f,x,2.7)));
fprintf('%0.8e = ea_x(2.74683993)\n\n',double(subs(ea_x,x,2.74683993)));

fprintf('%0.8e = f(1.75653738),(9d)\n', double(subs(f,x,1.75653738)));
fprintf('%0.8e = f(1.7565373),(8d)\n', double(subs(f,x,1.7565373)));
fprintf('%0.8e = f(1.756537),(7)\n', double(subs(f,x,1.756537)));
fprintf('%0.8e = f(1.75653),(6)\n', double(subs(f,x,1.75653)));
fprintf('%0.8e = f(1.7565),(5)\n', double(subs(f,x,1.7565)));
fprintf('%0.8e = f(1.756),(4)\n', double(subs(f,x,1.756)));
fprintf('%0.8e = f(1.75),(3)\n', double(subs(f,x,1.75)));
fprintf('%0.8e = f(1.7),(2)\n', double(subs(f,x,1.7)));
fprintf('%0.8e = ea_x(1.75653738)\n\n',double(subs(ea_x,x,1.75653738)));

fprintf('%0.8e = f(0.01123445),(9d)\n', double(subs(f,x,0.01123445)));
fprintf('%0.8e = f(0.0112344),(8d)\n', double(subs(f,x,0.0112344)));
fprintf('%0.8e = f(0.011234),(7)\n', double(subs(f,x,0.011234)));
fprintf('%0.8e = f(0.01123),(6)\n', double(subs(f,x,0.01123)));
fprintf('%0.8e = f(0.0112),(5)\n', double(subs(f,x,0.0112)));
fprintf('%0.8e = f(0.011),(4)\n', double(subs(f,x,0.011)));
fprintf('%0.8e = f(0.01),(3)\n', double(subs(f,x,0.01)));
fprintf('%0.8e = f(0.0),(2)\n', double(subs(f,x,0.0)));
fprintf('%0.8e = ea_x(0.01123445)\n\n',double(subs(ea_x,x,0.01123445)));
