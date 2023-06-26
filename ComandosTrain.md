ESPAÑOL BASELINE LITE
python ./FineTuning_bliteV2.py --model ResNetSE34L --log_input True --trainfunc angleproto --save_path exp/esp1 --scale 30 --margin 0.3 --premodel baseline_lite_ap.model --train_list ./Esp_List/Spanish_train.txt --test_list ./Esp_List/Spanish_test.txt --max_epoch 300 --train_path /var/data/db/FairVoice/FairVoice/FairVoice/Spanish --test_path /var/data/db/FairVoice/FairVoice/FairVoice/Spanish --newClases 486 --nPerSpeaker 2 


EPAÑOL BASELINE 2
python ./FineTuning_blit2V2.py --model ResNetSE34V2 --log_input True --encoder_type ASP --n_mels 64 --trainfunc softmaxproto --save_path exps/EspV2 --scale 30 --margin 0.3 --premodel baseline_v2_ap.model --train_list ./Esp_List/Spanish_train.txt --test_list ./Esp_List/Spanish_test.txt --max_epoch 300 --train_path /var/data/db/FairVoice/FairVoice/FairVoice/Spanish --test_path /var/data/db/FairVoice/FairVoice/FairVoice/Spanish --newClases 486  --nPerSpeaker 2 

PARA QSUB
qsub -q student.q@pcgtx1080 -l mem_free=10G /opt/Experimentos/AA/voxceleb_trainer/generic_python_qsub.sh /opt/Experimentos/AA/voxceleb_trainer/FineTuning_bliteV2.py 

qsub -q student.q@pcgtx1080 -l mem_free=10G /opt/Experimentos/AA/voxceleb_trainer/run_python.sh /opt/Experimentos/AA/voxceleb_trainer/FineTuning_blit2V2.py 


INGLES BASELINE LITE
python ./FineTuning_bliteV2.py --model ResNetSE34L --log_input True --trainfunc angleproto --save_path exp/eng1 --scale 30 --margin 0.3 --premodel baseline_lite_ap.model --train_list ./Eng_List2/English_train.txt --test_list ./Eng_List2/English_test.txt --max_epoch 400 --train_path /var/data/db/FairVoice/FairVoice/FairVoice/English --test_path /var/data/db/FairVoice/FairVoice/FairVoice/English --newClases 486 --nPerSpeaker 2  

INGLES BASELINE 2
python ./FineTuning_blit2V2.py --model ResNetSE34V2 --log_input True --encoder_type ASP --n_mels 64 --trainfunc softmaxproto --save_path exp/eng2 --scale 30 --margin 0.3 --premodel baseline_v2_ap.model --train_list ./Eng_list/English_train.txt --test_list ./Eng_list/English_test.txt --max_epoch 400 --train_path /var/data/db/FairVoice/FairVoice/FairVoice/English --test_path /var/data/db/FairVoice/FairVoice/FairVoice/English --newClases 1020 --nPerSpeaker 2 

PARA QSUB

qsub -q student.q@pcgtx1080.uam -l mem_free=10G /opt/Experimentos/AA/voxceleb_trainer/generic_python_qsub.sh ./opt/Experimentos/AA/voxceleb_trainer/FineTuning_bliteV2.py 


qsub -q student.q

python ./trainSpeakerNet.py --model ResNetSE34L --log_input True --encoder_type SAP --trainfunc amsoftmax --save_path trainEsp --nClasses 486 --batch_size 200 --scale 30 --margin 0.3 --train_list ./Esp_List/Spanish_train.txt --test_list ./Esp_List/Spanish_test.txt --max_epoch 300 --train_path /var/data/db/FairVoice/FairVoice/FairVoice/Spanish --test_path /var/data/db/FairVoice/FairVoice/FairVoice/Spanish  --nPerSpeaker 2 