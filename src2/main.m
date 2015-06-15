% Training data images
data_list = '../data/data5k.txt';
data_path = '../data/image/';

% Evaluation data images
test_list = '../data/query.txt';
test_path = '../data/image/';

% Training phase
training=true;
kmeans_model = '../data/kmeans_model.mat';
feature_model = '../data/final_feature.mat';
svm_model = '../data/svm_model.mat';

% Parameters
image_max_side = 50;
kmeans_max_sample = 1000000;
kmeans_k = 100;

% Output
result_file = '../result/res.txt';

%-----------------------------------------
if training
        labels_data = get_label(data_list);
        img_data = read_and_resize(data_list, data_path, image_max_side, image_max_side);
        patch_data = patch_images(img_data);
        patch_data_r = sample_reduce(patch_data, kmeans_max_sample);
        kms = kmeans_train(patch_data_r, kmeans_k);
        save(kmeans_model, 'kms');
        f1 = kmeans_feature(patch_data, kms);
        f2 = cmhsv_feature(img_data);
        f = [f1 f2];
        save(feature_model, 'f');
        svms = train_svm(f, labels_data);
        save(svm_model, 'svms');
else
        load(kmeans_model, 'kms');
        load(feature_model, 'f');
        load(svm_model, 'svms');
end
labels_test = get_label(test_list);
img_test = read_and_resize(test_list, test_path, image_max_side, image_max_side);
patch_test = patch_images(img_test);
g1 = kmeans_feature(patch_test, kms);
g2 = cmhsv_feature(img_test);
g = [g1 g2];
predict_label = predict_svm(svms, g);

dlmwrite(result_file, [predict_label g]);
