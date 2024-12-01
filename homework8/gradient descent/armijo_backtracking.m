function alpha_k = armijo_backtracking(f,x,d,alpha,beta,t)
    alpha_k = t;
    while ? %======TODO:write Armijo condition vialation here after "while" ========    
        alpha_k = alpha_k * beta; % update the step size
    end
end

