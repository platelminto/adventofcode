data = readmatrix("data/day1.txt");
sorted1 = sort(data(:, 1));
sorted2 = sort(data(:, 2));

listDistance = sum(abs(sorted1 - sorted2))

counts = arrayfun(@(x) sum(data(:, 2) == x), data(:, 1));

similarityScore = sum(data(:, 1) .* counts)