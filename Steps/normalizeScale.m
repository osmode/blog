train_data = dlmread('output2');

num_train = size(train_data,1);
num_col = size(train_data,2);

% store means and standard deviations of each column as a num_train x 1 vector
% with each row corresponding to a column in train_data 
% mean normalize and scale train data
means = [];
stds = [];
temp_mean = [];
temp_std = [];

for i = 1:size(train_data,2),
	temp_mean = mean(train_data(:,i));
	temp_std = std(train_data(:,i));

	means = [means; temp_mean];
	stds = [stds; temp_std];
end;

for j = 1:size(train_data,1),
	for i = 1:size(train_data,2),
		train_data(j,i) = ( 1.0*train_data(j,i) - means(i) ) / stds(i);
		
	end;
end;


% write the data to disk in csv format
dlmwrite('output3',train_data);
disp(means);
disp(stds);


