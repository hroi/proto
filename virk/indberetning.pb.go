// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.21.0
// 	protoc        v3.11.4
// source: virk/indberetning.proto

package virk

import (
	proto "github.com/golang/protobuf/proto"
	types "github.com/hroi/proto/types"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// This is a compile-time assertion that a sufficiently up-to-date version
// of the legacy proto package is being used.
const _ = proto.ProtoPackageIsVersion4

type Indberetning struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	IndberetningId   int64            `protobuf:"varint,1,opt,name=indberetning_id,json=indberetningId,proto3" json:"indberetning_id,omitempty"`
	XId              string           `protobuf:"bytes,2,opt,name=_id,json=Id,proto3" json:"_id,omitempty"`
	Sagsnummer       string           `protobuf:"bytes,3,opt,name=sagsnummer,proto3" json:"sagsnummer,omitempty"`
	Regnskabsperiode *types.Daterange `protobuf:"bytes,4,opt,name=regnskabsperiode,proto3" json:"regnskabsperiode,omitempty"`
}

func (x *Indberetning) Reset() {
	*x = Indberetning{}
	if protoimpl.UnsafeEnabled {
		mi := &file_virk_indberetning_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *Indberetning) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Indberetning) ProtoMessage() {}

func (x *Indberetning) ProtoReflect() protoreflect.Message {
	mi := &file_virk_indberetning_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Indberetning.ProtoReflect.Descriptor instead.
func (*Indberetning) Descriptor() ([]byte, []int) {
	return file_virk_indberetning_proto_rawDescGZIP(), []int{0}
}

func (x *Indberetning) GetIndberetningId() int64 {
	if x != nil {
		return x.IndberetningId
	}
	return 0
}

func (x *Indberetning) GetXId() string {
	if x != nil {
		return x.XId
	}
	return ""
}

func (x *Indberetning) GetSagsnummer() string {
	if x != nil {
		return x.Sagsnummer
	}
	return ""
}

func (x *Indberetning) GetRegnskabsperiode() *types.Daterange {
	if x != nil {
		return x.Regnskabsperiode
	}
	return nil
}

var File_virk_indberetning_proto protoreflect.FileDescriptor

var file_virk_indberetning_proto_rawDesc = []byte{
	0x0a, 0x17, 0x76, 0x69, 0x72, 0x6b, 0x2f, 0x69, 0x6e, 0x64, 0x62, 0x65, 0x72, 0x65, 0x74, 0x6e,
	0x69, 0x6e, 0x67, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x09, 0x61, 0x73, 0x64, 0x66, 0x2e,
	0x76, 0x69, 0x72, 0x6b, 0x1a, 0x0b, 0x74, 0x79, 0x70, 0x65, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x22, 0xab, 0x01, 0x0a, 0x0c, 0x49, 0x6e, 0x64, 0x62, 0x65, 0x72, 0x65, 0x74, 0x6e, 0x69,
	0x6e, 0x67, 0x12, 0x27, 0x0a, 0x0f, 0x69, 0x6e, 0x64, 0x62, 0x65, 0x72, 0x65, 0x74, 0x6e, 0x69,
	0x6e, 0x67, 0x5f, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x03, 0x52, 0x0e, 0x69, 0x6e, 0x64,
	0x62, 0x65, 0x72, 0x65, 0x74, 0x6e, 0x69, 0x6e, 0x67, 0x49, 0x64, 0x12, 0x0f, 0x0a, 0x03, 0x5f,
	0x69, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x02, 0x49, 0x64, 0x12, 0x1e, 0x0a, 0x0a,
	0x73, 0x61, 0x67, 0x73, 0x6e, 0x75, 0x6d, 0x6d, 0x65, 0x72, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x0a, 0x73, 0x61, 0x67, 0x73, 0x6e, 0x75, 0x6d, 0x6d, 0x65, 0x72, 0x12, 0x41, 0x0a, 0x10,
	0x72, 0x65, 0x67, 0x6e, 0x73, 0x6b, 0x61, 0x62, 0x73, 0x70, 0x65, 0x72, 0x69, 0x6f, 0x64, 0x65,
	0x18, 0x04, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x15, 0x2e, 0x61, 0x73, 0x64, 0x66, 0x2e, 0x74, 0x79,
	0x70, 0x65, 0x73, 0x2e, 0x44, 0x61, 0x74, 0x65, 0x72, 0x61, 0x6e, 0x67, 0x65, 0x52, 0x10, 0x72,
	0x65, 0x67, 0x6e, 0x73, 0x6b, 0x61, 0x62, 0x73, 0x70, 0x65, 0x72, 0x69, 0x6f, 0x64, 0x65, 0x42,
	0x1c, 0x5a, 0x1a, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x68, 0x72,
	0x6f, 0x69, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2f, 0x76, 0x69, 0x72, 0x6b, 0x62, 0x06, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_virk_indberetning_proto_rawDescOnce sync.Once
	file_virk_indberetning_proto_rawDescData = file_virk_indberetning_proto_rawDesc
)

func file_virk_indberetning_proto_rawDescGZIP() []byte {
	file_virk_indberetning_proto_rawDescOnce.Do(func() {
		file_virk_indberetning_proto_rawDescData = protoimpl.X.CompressGZIP(file_virk_indberetning_proto_rawDescData)
	})
	return file_virk_indberetning_proto_rawDescData
}

var file_virk_indberetning_proto_msgTypes = make([]protoimpl.MessageInfo, 1)
var file_virk_indberetning_proto_goTypes = []interface{}{
	(*Indberetning)(nil),    // 0: asdf.virk.Indberetning
	(*types.Daterange)(nil), // 1: asdf.types.Daterange
}
var file_virk_indberetning_proto_depIdxs = []int32{
	1, // 0: asdf.virk.Indberetning.regnskabsperiode:type_name -> asdf.types.Daterange
	1, // [1:1] is the sub-list for method output_type
	1, // [1:1] is the sub-list for method input_type
	1, // [1:1] is the sub-list for extension type_name
	1, // [1:1] is the sub-list for extension extendee
	0, // [0:1] is the sub-list for field type_name
}

func init() { file_virk_indberetning_proto_init() }
func file_virk_indberetning_proto_init() {
	if File_virk_indberetning_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_virk_indberetning_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*Indberetning); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_virk_indberetning_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   1,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_virk_indberetning_proto_goTypes,
		DependencyIndexes: file_virk_indberetning_proto_depIdxs,
		MessageInfos:      file_virk_indberetning_proto_msgTypes,
	}.Build()
	File_virk_indberetning_proto = out.File
	file_virk_indberetning_proto_rawDesc = nil
	file_virk_indberetning_proto_goTypes = nil
	file_virk_indberetning_proto_depIdxs = nil
}