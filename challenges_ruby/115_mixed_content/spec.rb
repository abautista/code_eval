require('minitest/autorun')
require_relative('mixed_content')

describe "separate function" do
  it "separates digits from words" do
    input = %w[8 33 21]
    output = {
      words: [],
      digits: %w[8 33 21]
    }
    separate(input).must_equal output
  end
end
