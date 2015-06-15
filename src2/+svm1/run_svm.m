addpath minFunc;
PATH        = 'D:\v-qifen\expr\cifar-mlayer\mlayer-morepatch\joke\';
TRAIN_FNAME = [PATH 'train.bin'];
TEST_FNAME  = [PATH 'test.bin'];
DIM         = 289;
TRAIN_N     = 1341;
TEST_N      = 1341;

% load train
fprintf('Reading train data...\n');
tic;
[X0, Y0] = read_data(TRAIN_FNAME, TRAIN_N, DIM);
toc;
fprintf('\n');

XMean = mean(X0);
XSD = sqrt(var(X0)+0.01);
X0 = bsxfun(@rdivide, bsxfun(@minus, X0, XMean), XSD);
X0 = [X0, ones(size(X0,1),1)];

% train classifier using SVM
fprintf('Training...\n');
tic;
C = 1;
T = train_svm(X0, Y0, C);
toc;

[val,labels] = max(X0*T, [], 2);
fprintf('Train accuracy %f%%\n', 100 * (1 - sum(labels ~= Y0) / length(Y0)));
fprintf('\n');


% load test
fprintf('Reading test data...\n');
tic;
[X, Y] = read_data(TEST_FNAME, TEST_N, DIM);
toc;

X = bsxfun(@rdivide, bsxfun(@minus, X, XMean), XSD);
X = [X, ones(size(X,1),1)];

% test and print result
[val,labels] = max(X*T, [], 2);
fprintf('Test accuracy %f%%\n', 100 * (1 - sum(labels ~= Y) / length(Y)));
fprintf('\n');


% done
fprintf('Done.\n');