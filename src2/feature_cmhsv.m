% sample image
%  n07897438_3661.JPEG
%  4610 1254 6178 3666 1688 1898 3788 2308 2251

% function: get color moments feature of an image
%   [in] img: num*n*m*3 doubles, in range [0, 1]
%   [out] f:  num*k doubles
function features = feature_cmhsv(img_data)
    num = size(img_data, 1);
    features = zeros(num, 18);
    for i = 1:num
        img = img_data{i, 1};
        assert(size(size(img), 2) == 3); % n*m*k doubles
        assert(size(img, 3) == 3); % n*m*3 doubles

        data_rgb = reshape(img, [], 3);
        data_hsv = rgb2hsv(data_rgb);
        data = [data_rgb data_hsv];

        m = mean(data);
        r = std(data);
        s = skewness(data);
        features(i, :) = [m r s];
    end
end
