% usage:
%  train_svm(NxM features, Nx1 class)
function model = train_svm(f, labels)
    model = libsvmtrain(labels, f)
end
