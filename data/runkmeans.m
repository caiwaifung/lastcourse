% change dir here
a = [];
p = dir('KMeans/*.txt');
num = length(p)

for i = 1 : num
        i
        s = p(i).name
        a = [a; dlmread(strcat('KMeans/', s))];
end


[ix,k4] = kmeans(a,4);
dlmwrite('kmeans4.txt', k4);
[ix,k8] = kmeans(a,8);
dlmwrite('kmeans8.txt', k8);
[ix,k12] = kmeans(a,12);
dlmwrite('kmeans12.txt', k12);
[ix,k16] = kmeans(a,16);
dlmwrite('kmeans16.txt', k16);
[ix,k20] = kmeans(a,20);
dlmwrite('kmeans20.txt', k20);
[ix,k24] = kmeans(a,24);
dlmwrite('kmeans24.txt', k24);

% See after-pca.py
