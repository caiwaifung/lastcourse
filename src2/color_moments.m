% sample image
%  n07897438_3661.JPEG
%  4610 1254 6178 3666 1688 1898 3788 2308 2251

% function: get color moments feature of an image
%   [in] img: n*m*3 doubles
%   [out] f:  1*k doubles
function feature = color_moments(img)
    assert(size(size(img), 2) == 3); % n*m*k doubles
    assert(size(img, 3) == 3); % n*m*3 doubles

    data_rgb = double(reshape(img, [], 3)) / 256;
    data_hsv = rgb2hsv(data_rgb);
    data = [data_rgb data_hsv];

    m = mean(data);
    r = std(data);
    s = skewness(data);
    %s = nthroot(mean((data - m).^3), 3);

    feature = [m r s];
end
