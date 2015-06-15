function model = train_svm(f, labels)
model = libsvmtrain(labels, f)
