% usage:
%  extract_patches(cell array of 50x50x3 double 0~1 images)
%  {n_patches x 108} double mean=0 var=1
function patch = extract_patches(data)
    n = size(data, 1);
    res = cell(n,1);
    progress.textprogressbar('again: ');
    for i = 1:n
        progress.textprogressbar(100*i/n);
        cnt=0;
        im = data{i,1};
        h = size(im,1);
        w = size(im,2);
        assert(size(im,3) == 3);
        m = (h-5)*(w-5);
        j = 0;
        cur = zeros(m, 108);
        for x = 1 : h-5
            for y = 1 : w-5
                j = j + 1;
                sub = reshape(im(x:x+5, y:y+5, :), 1, []);
                cur(j, :) = sub;
            end
        end
        cur = bsxfun(@minus, cur, mean(cur')');
        cur = normr(cur);
        res{i,1} = cur;
    end
    
    progress.textprogressbar('done');
    patch = res;
end
