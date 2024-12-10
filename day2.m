lines = readlines("data/day2.txt");
data = cellfun(@(x) str2num(x), lines, 'UniformOutput', false);


function isIncreasing = isIncreasing(vec)
    diffs = diff(vec);
    isIncreasing = all(diffs >= 1 & diffs <= 3);
end

function isDecreasing = isDecreasing(vec)
    diffs = diff(vec);
    isDecreasing = all(diffs <= -1 & diffs >= -3);
end

isInc = cellfun(@isIncreasing, data);
isDec = cellfun(@isDecreasing, data);

countBothTrue = sum(isInc | isDec)