% sample usage:
%  read_and_resize('data/5k.txt', 'data/image/', 50, 50)
%  return n x 50 x 50 x 3   double 0~1
function img = read_and_resize(file_list, file_path, max_width, max_height)

