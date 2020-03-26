function compute_stats(paths,titles,orig_path,gray)
addpath('matlab_libs')
orig = imread(orig_path);
if gray== true
    orig2 = rgb2gray(orig);
    orig(:,:,1) = orig2;
    orig(:,:,2) = orig2;
    orig(:,:,3) = orig2;
end
titles = convertCharsToStrings(titles);
paths = convertCharsToStrings(paths);
for i= 1:length(paths)
    img = imread(paths(i));
    if gray== true
        img2(:,:,1)= img;
        img2(:,:,2)= img;
        img2(:,:,3)= img;
        r_mse = mean((double(img)-double(orig2)).^2,'All');
        r_psnr = psnr(img,orig2);
        r_ssim = ssim(img,orig2);
        %r_summer = SUMMER(orig2,img);
        r_unique = mslUNIQUE(img2,orig);
    else
        r_mse = mean((double(img)-double(orig)).^2,'All');
        r_psnr = psnr(img,orig);
        r_ssim = ssim(img,orig);
        r_summer = SUMMER(orig,img);
        r_unique = mslUNIQUE(img,orig);
    end
    
    fprintf("\n %s \n",titles(i));
    fprintf("MSE: %.4f\n",r_mse);
    fprintf("PSNR: %.4f\n",r_psnr);
    fprintf("SSIM: %.4f\n",r_ssim);
    if gray == false
        fprintf("SUMMER: %.4f\n",r_summer);
    end
    fprintf("UNIQUE: %.4f\n",r_unique);
end

