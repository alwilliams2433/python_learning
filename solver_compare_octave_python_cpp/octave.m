size = 1_000;

tic;
matrix = rand(size,size);
independent = rand(size,1);
constructionTime = toc;

tic;
solution = matrix\independent;
solutionTime = toc;

disp('construction time:')
disp(constructionTime)
disp('solution time:')
disp(solutionTime)

error2 = norm(matrix*solution - independent)
errorInf = norm(matrix*solution - independent, inf)
