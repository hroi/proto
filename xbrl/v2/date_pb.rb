# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xbrl/v2/date.proto

require 'google/protobuf'

Google::Protobuf::DescriptorPool.generated_pool.build do
  add_file("xbrl/v2/date.proto", :syntax => :proto3) do
    add_message "asdf.xbrl.v2.Date" do
      optional :year, :int32, 1
      optional :month, :int32, 2
      optional :day, :int32, 3
    end
    add_message "asdf.xbrl.v2.Duration" do
      optional :start, :message, 1, "asdf.xbrl.v2.Date"
      optional :end, :message, 2, "asdf.xbrl.v2.Date"
    end
  end
end

module Asdf
  module Xbrl
    module V2
      Date = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("asdf.xbrl.v2.Date").msgclass
      Duration = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("asdf.xbrl.v2.Duration").msgclass
    end
  end
end