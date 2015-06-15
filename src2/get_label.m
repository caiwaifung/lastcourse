% sample usage:
%  get_labels('data/5k.txt')
%  [0; 0; 0; 1; 1; 1; 2; 2; 1; 5; 6; 9; 1; 8; ...]
function labels = get_label(file_list)
fid = fopen(file_list);
lines = textscan(fid,'%s','Delimiter','\n');
fclose(fid);
n = size(lines{1},1);
res=zeros(n,1);

for i = 1:n
        t = strsplit(lines{1}{i}, '_');
        t = t{1};
        if strcmp(t, 'n01613177')
                res(i,1) = 0;
        elseif strcmp(t, 'n01923025')
                res(i,1) = 1;
        elseif strcmp(t, 'n02278980')
                res(i,1) = 2;
        elseif strcmp(t, 'n03767203')
                res(i,1) = 3;
        elseif strcmp(t, 'n03877845')
                res(i,1) = 4;
        elseif strcmp(t, 'n04515003')
                res(i,1) = 5;
        elseif strcmp(t, 'n04583620')
                res(i,1) = 6;
        elseif strcmp(t, 'n07897438')
                res(i,1) = 7;
        elseif strcmp(t, 'n10247358')
                res(i,1) = 8;
        elseif strcmp(t, 'n11669921')
                res(i,1) = 9;
        end
end
labels = res;
end
