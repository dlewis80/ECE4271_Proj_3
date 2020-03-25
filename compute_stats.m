function compute_stats(paths,titles,orig_path)
addpath('matlab_libs')
orig = imread(orig_path);
titles = convertCharsToStrings(titles);
paths = convertCharsToStrings(paths);
for i= 1:length(paths)
    img = imread(paths(i));
    r_mse = mean((double(img)-double(orig)).^2,'All');
    r_psnr = psnr(img,orig);
    r_ssim = ssim(rgb2gray(img),rgb2gray(orig));
    r_summer = SUMMER(orig,img);
    r_unique = mslUNIQUE(img,orig);
    fprintf("\n %s \n",titles(i));
    fprintf("MSE: %.4f\n",r_mse);
    fprintf("PSNR: %.4f\n",r_psnr);
    fprintf("SSIM: %.4f\n",r_ssim);
    fprintf("SUMMER: %.4f\n",r_summer);
    fprintf("UNIQUE: %.4f\n",r_unique);
end

