# DeepTag dataset

## File structure
There are 700 folders. 
Each folder contains 100 images of the same marker, view distance, and view angle.

Folder names are in the format of `imgs_0ABC`, where
- "A" is the marker family, and 0~6 represents AprilTag, ArUco, ARToolKitPlus, TopoTag, AprilTag-XO, AprilTag-XA and RuneTag(+) respectively.
- "B" is the view angle, and 0~9 represents 0, 10, 20, 30, 40, 50, 60, 65, 70, and 75 deg respectively.
- "C" is the view distance, and 0~9 represents 10, 20, 30, 40, 50, 60, 70, 80, 90, and 100 cm respectively.


## Terms of use
The dataset is provided for research purposes only. Any commercial use is prohibited. When using the dataset in your research work, please cite the following paper:

	"DeepTag: A General Framework for Fiducial Marker Design and Detection." 
	Zhuming Zhang, Yongtao Hu, Guoxing Yu, and Jingwen Dai  
	IEEE TPAMI 2023.

	@article{zhang2023deeptag,
	  title={{DeepTag: A General Framework for Fiducial Marker Design and Detection}},
	  author={Zhang, Zhuming and Hu, Yongtao and Yu, Guoxing and Dai, Jingwen},
	  journal={IEEE Transactions on Pattern Analysis and Machine Intelligence},
	  volume={45},
	  number={3},
	  pages={2931-2944},
	  year={2023},
	  publisher={IEEE}
	}
