% usage:
%  predict_svm(model, NxM features, Nx1 true label for eval)
%  Nx1 predicted label
function label = predict_svm(model, f, ground_truth)
    %[val, labels] = max(f * model, [], 2);
    %fprintf('Train accuracy %f%%\n', 100 * (1 - sum(labels ~= ground_truth) / length(ground_truth)));
    %label = labels;

    label = libsvmpredict(ground_truth, f, model);
end

