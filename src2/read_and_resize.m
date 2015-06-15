% sample usage:
%  read_and_resize('data/5k.txt', 'data/image/', 50, 50)
%  return cell array of {50h x 50w x 3}   double 0~1
function img = read_and_resize(file_list, file_path, max_width, max_height)
    fid = fopen(file_list);
    lines = textscan(fid,'%s','Delimiter','\n');
    fclose(fid);
    n = size(lines{1},1);
    res = cell(n,1);
    progress.textprogressbar('files: ');
    for i = 1:n
        progress.textprogressbar(100*i/n);
        f = lines{1}{i};
        f = [file_path f];
        im = imread(f);
        w=size(im,2);
        h=size(im,1);
        im = imresize(im, min(double(max_width)/w, double(max_height)/h));
        res{i,1} = double(im) / 256;
    end
    img = res;
    progress.textprogressbar('done');
end
