%common parameters
%======TODO: input the value for the question marks======
x = ?;                  %initial point
epsilon = ?;            % stopping  criteira
maxiter = 200;          % max iteration
iter = 0;

%parameters for Armijo backtraking
sigma = ?;             
gamma = ?;
t = 1;  %initial step size in line search
%========================================================

%function
f = @(x) exp(1-x(1)-x(2))+ exp(x(1)+x(2)-1)+x(1)^2+x(1)*x(2)+x(2)^2+x(1)-3*x(2);

%plot the contour of cost function:
x1 =  -2.5:0.01:0.5;
x2 =   0:0.01:3;
n=length(x1);
z=zeros(n,n);
for i=1:n
    for j=1:n
        z(n+1-i,n+1-j)=f([x1(i),x2(j)]);
    end
end
figure(1)
contour(x1,x2,z,20);
hold on

%Newton's method
while norm(gradient(x)) > epsilon  && iter<=maxiter
    %======TODO:form the search direction d using the "gradient.m" and "hessian.m" functions===
    d = ?;
    %=============================================================
    
    %=====TODO: Assign the step size using the "armijo_backtracking.m" function==
    alpha_k = ?; %armijo backtracking 
    %=============================================================
    
    %==============TODO: Newton's update x to x_temp===============
    xtemp = ?;
    %========================================================
    
    % Make plots
    plot(x(1), x(2), '*r');
    hold on;
    plot([x(1), xtemp(1)], [x(2), xtemp(2)], '-g');
    hold on;
    % Output the solution in each step
    
    iter = iter + 1;
    x = xtemp;
end
fprintf('The algorithm ends after %d iterations\n x*=[%f,%f]\n f(x*)=%f\n gradient norm=%e\n',iter,x,f(x),norm(gradient(x)));
