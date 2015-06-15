% usage:
%  train_svm(NxM features, Nx1 class)
function model = train_svm(f, labels)
    %model = svm1.train_svm(f, labels, 1);
    model = libsvmtrain(labels, f, '-t 0');
end
