dataset_paths = {
	'celeba_train': '',
	'celeba_test': '/workspace/celeba_hq_256',
	'celeba_train_sketch': '',
	'celeba_test_sketch': '',
	'celeba_train_segmentation': '',
	'celeba_test_segmentation': '',
	'ffhq': '/workspace/ffhq-256',
}

model_paths = {
	'ir_se50': 'pretrained_models/model_ir_se50.pth',
	'circular_face': 'pretrained_models/CurricularFace_Backbone.pth',
	'mtcnn_pnet': 'pretrained_models/mtcnn/pnet.npy',
	'mtcnn_rnet': 'pretrained_models/mtcnn/rnet.npy',
	'mtcnn_onet': 'pretrained_models/mtcnn/onet.npy',
	'shape_predictor': 'shape_predictor_68_face_landmarks.dat',
	'moco': 'pretrained_models/moco_v2_800ep_pretrain.pth.tar',
	'eg3d_ffhq': 'pretrained_models/ffhq512-128.pkl',
	'eg3d_pth': 'pretrained_models/ffhq512-64.pth'
}
