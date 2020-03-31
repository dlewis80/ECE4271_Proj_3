close all

orig_img = imread('Data_students/blurryImage.png');
K = orig_img;
figure
imshow(K)

K = imsharpen(K,'Radius',15,'Amount',3);
for x = 1:3
    K(:,:,x) = medfilt2(medfilt2(K(:,:,x)),[5,5]);
end
figure
imshow(K)

K = imsharpen(K,'Radius',5,'Amount',2);
for x = 1:3
    K(:,:,x) = medfilt2(medfilt2(K(:,:,x)),[5,5]);
end
figure
imshow(K)
