# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xbrl/v2/entity.proto

require 'google/protobuf'

Google::Protobuf::DescriptorPool.generated_pool.build do
  add_file("xbrl/v2/entity.proto", :syntax => :proto3) do
    add_message "asdf.xbrl.v2.Entity" do
      optional :scheme, :string, 1
      optional :identifier, :string, 2
    end
  end
end

module Asdf
  module Xbrl
    module V2
      Entity = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("asdf.xbrl.v2.Entity").msgclass
    end
  end
end
