#!/usr/bin/env ruby

def get_change(purchase_price, cash)
  
  bill_values = {
    'ONE HUNDRED' => 100.00,
    'FIFTY' => 50,
    'TWENTY' => 20,
    'TEN' => 10,
    'FIVE' => 5,
    'TWO' => 2,
    'ONE' => 1,
    'HALF DOLLAR' => 0.50,
    'QUARTER' => 0.25,
    'DIME' => 0.10,
    'NICKEL' => 0.05,
    'PENNY' => 0.01
  }
  
  result = []
  change = (cash - purchase_price).round(2)
    
  bill_values.each do |key, value|

    coins_number = (change / value).round(2)
    
    if coins_number != 0
      result = result + [key] * coins_number
      change = (change % value).round(2)
    end
  end
  result.join(",")
end

File.open(ARGV[0]).each_line do |line|
  purchase_price, cash = line.chop.split(";")
  if Float(purchase_price) == Float(cash)
    puts "ZERO"
  elsif Float(purchase_price) > Float(cash)
    puts "ERROR"
  else
    change = get_change(Float(purchase_price), Float(cash))
    puts change
  end
end








