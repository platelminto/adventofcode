function data = getData(filename)
    filepath = fullfile('data', filename);
    data = fileread(filepath);