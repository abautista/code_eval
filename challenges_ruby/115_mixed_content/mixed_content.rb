#!/usr/bin/env ruby

def separate(items)
  pattern = /^\d+$/
  items.reduce({ words: [], digits: [] }) do |result, item|
    if pattern =~ item
      result[:digits] << item
    else
      result[:words] << item
    end
    result
  end
end

if __FILE__ == $0
  File.open(ARGV[0]).each_line do |line|
    result = separate line.chomp.split(",")
    
    if result[:words].empty?
      puts "#{result[:digits].join(",")}"
    elsif result[:digits].empty?
      puts "#{result[:words].join(",")}"
    else
      puts "#{result[:words].join(",")}|#{result[:digits].join(",")}"
    end
  end
end
