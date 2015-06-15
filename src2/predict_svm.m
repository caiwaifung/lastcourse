function label = predict_svm(model, f, ground_truth)
label = libsvmpredict(ground_truth, f, model);

