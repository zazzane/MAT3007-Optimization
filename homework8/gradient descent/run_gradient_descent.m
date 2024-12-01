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

%This will allow one to choose an algorithm in the command window by
%inputing 1,2,or 3.
prompt = 'Which strategy to use?\n [1]: large constant stepsize\n [2]: small constant stepsize\n [3]: armijo backtracking\n';
s = input(prompt);

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
%gradient descent algorithm:
while norm(gradient(x)) > epsilon && iter<=maxiter
    %======TODO:form the search direction d using the "gradient.m" function===
    d =  ?;
    %========================================================
    
    %=====TODO: Assign different step sizes==============
    if s==1
        alpha_k = ?;       %large constant step size
    elseif s==2
        alpha_k = ?;     %small constant step size
    else 
        alpha_k = ?; %armijo backtracking using the "armijo_backtracking.m" function
    end
    %========================================================
    
    %==============TODO: GD update x to x_temp===============
    xtemp = ?;
    %========================================================
    
    % Make some plots
    plot(x(1), x(2), '*r');
    hold on;
    plot([x(1), xtemp(1)], [x(2), xtemp(2)], '-g');
    hold on;
    % Output the solution in each step
    iter = iter + 1;
    x = xtemp;
end

%This is to print some final information
fprintf('The algorithm ends after %d iterations\n x*=[%f,%f]\n f(x*)=%f\n gradient norm=%e\n',iter,x,f(x),norm(gradient(x)));
