% Training data images
data_list = '../data/data20.txt';
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
kmeans_max_sample = 1000;
kmeans_k = 100;

% Output
result_file = '../result/res.txt';

% Training
if training
    % read the data & labels
    labels_data = get_label(data_list);
    fprintf('> label got.\n');
    img_data = read_and_resize(data_list, data_path, image_max_side, image_max_side);
    fprintf('> resized.\n');
    whos labels_data img_data;
    % extract patches
    patch_data = extract_patches(img_data); % num*(N-W+1)^2*P
    fprintf('> extracted.\n');
    whos patch_data;
    patch_data_r = sample_patches(patch_data, kmeans_max_sample); % snum*P
    fprintf('> sampled.\n');
    whos patch_data_r;
    % run kmeans
    kms = kmeans_train(patch_data_r, kmeans_k); % matrix of K*P where P=W*W*3
    save(kmeans_model, 'kms');
    fprintf('> kmeans finished.\n');
    whos kms;
    % extract features
    f1 = feature_kmeans(patch_data, kms);
    fprintf('> kmeans featured.\n');
    whos f1;
    f2 = feature_cmhsv(img_data);
    fprintf('> cm featured.\n');
    whos f2;
    f = [f1 f2];
    save(feature_model, 'f');
    whos f;

    svms = train_svm(f, labels_data);
    predict_svm(svms, f, labels_data);
    save(svm_model, 'svms');

    fprintf('> svm trained.\n');
    whos svms;

else
    load(kmeans_model, 'kms');
    load(feature_model, 'f');
    load(svm_model, 'svms');
end

% Main phase
%  now we have: f (features), kms (kmeans model), svms (svm model)
labels_test = get_label(test_list);
img_test = read_and_resize(test_list, test_path, image_max_side, image_max_side);
patch_test = extract_patches(img_test);
g1 = feature_kmeans(patch_test, kms);
g2 = feature_cmhsv(img_test);
g = [g1 g2];
predict_label = predict_svm(svms, g, labels_test);

dlmwrite(result_file, [predict_label g]);
