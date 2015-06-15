function patches = sample_patches(data, limit)
    num = size(data, 1);
    patches = zeros(limit, 108);
    for i = 1:limit
        j = randi(num);
        k = randi(size(data{j, 1}, 1));
        assert(size(data{j, 1}, 2) == 108);
        patches(i, :) = data{j, 1}(k, :);
    end
end

