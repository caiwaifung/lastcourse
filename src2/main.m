clear

% Training data images
data_list = '../data/data1k.txt';
data_path = '../data/image/';

% Evaluation data images
test_list = '../data/query.txt';
test_path = '../data/image/';

% For training phase
training=true;
kmeans_model = '../data/kmeans_model.mat';
feature_model = '../data/final_feature.mat';
svm_model = '../data/svm_model.mat';

% Parameters
image_max_side = 50;
kmeans_max_sample = 100000;
kmeans_k = 100;
feature_coeff = [1 20];

% Output
result_file = '../result/res.txt';
addpath minFunc;

% Training
if training
    % read the data & labels
    fprintf('> getting labels...\n');
    labels_data = get_label(data_list);
    fprintf('> reading images and resizing...\n');
    img_data = read_and_resize(data_list, data_path, image_max_side, image_max_side);

    % extract patches
    fprintf('> extracting patches...\n');
    patch_data = extract_patches(img_data); % num*(N-W+1)^2*P

    %whos patch_data;
    fprintf('> sampling...\n');
    patch_data_r = sample_patches(patch_data, kmeans_max_sample); % snum*P

    % run kmeans
    fprintf('> k-means clustering...\n');
    kms = kmeans_train(patch_data_r, kmeans_k); % matrix of K*P where P=W*W*3
    save(kmeans_model, 'kms');
    whos kms;
    visualize_kmeans;

    % extract features
    fprintf('> calculating k-means feature...\n');
    f1 = feature_kmeans(patch_data, kms);

    f1 = f1 * feature_coeff(1);
    %whos f1;
    
    fprintf('> calculating color feature...\n');
    f2 = feature_cmhsv(img_data);
    f2 = f2 * feature_coeff(2);
    %whos f2;

    f = [f1 f2];
    save(feature_model, 'f');
    
    fprintf('> training svm...\n');
    svms = train_svm(f, labels_data);
    predict_svm(svms, f, labels_data);
    save(svm_model, 'svms');
    
    fprintf('------------ done training -----------\n');
else
    fprintf('> loading models...\n');
    load(kmeans_model, 'kms');
    load(feature_model, 'f');
    load(svm_model, 'svms');
end

% Main phase
%  now we have: f (features), kms (kmeans model), svms (svm model)

fprintf('> geting ground truth labels...\n');
labels_test = get_label(test_list);

fprintf('> reading and resizing test images...\n');
img_test = read_and_resize(test_list, test_path, image_max_side, image_max_side);

fprintf('> extracting patches for test images...\n');
patch_test = extract_patches(img_test);

fprintf('> calculating features for test images...\n');
g1 = feature_kmeans(patch_test, kms);
g1 = g1 * feature_coeff(1);
g2 = feature_cmhsv(img_test);
g2 = g2 * feature_coeff(2);
g = [g1 g2];

fprintf('> classifying by svm...\n');
predict_label = predict_svm(svms, g, labels_test);

dlmwrite(result_file, [predict_label g]);

fprintf('------------ done evaluation -----------\n');
