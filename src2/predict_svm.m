% usage:
%  predict_svm(model, NxM features, Nx1 true label for eval)
%  Nx1 predicted label
function label = predict_svm(model, f, ground_truth)
    label = libsvmpredict(ground_truth, f, model);
end

