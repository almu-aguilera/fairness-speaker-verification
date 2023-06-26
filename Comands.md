----------------------------------------------------------------------------------------------------------------
------------------------------------VOXCELEB---------------------------------------------------------------
- AM-Softmax:
python ./trainSpeakerNet.py --model ResNetSE34L --log_input True --encoder_type SAP --trainfunc amsoftmax --save_path exps/exp1 --nClasses 5994 --batch_size 200 --scale 30 --margin 0.3

- Angular prototypical:
python ./trainSpeakerNet.py --model ResNetSE34L --log_input True --encoder_type SAP --trainfunc angleproto --save_path exps/exp2 --nPerSpeaker 2 --batch_size 200

- PreTrain Models
python ./trainSpeakerNet.py --eval --model ResNetSE34V2 --log_input True --encoder_type ASP --n_mels 64 --trainfunc softmaxproto --save_path exps/test --eval_frames 400  --initial_model baseline_v2_ap.model

python ./trainSpeakerNet.py --eval --model ResNetSE34L --log_input True --trainfunc angleproto --save_path exps/test --eval_frames 400 --initial_model baseline_lite_ap.model


----------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------

---TESTEAR ESP---
python ./trainSpeakerNet.py --eval --model ResNetSE34V2 --log_input True --encoder_type ASP --n_mels 64 --trainfunc softmaxproto --save_path exps/test1 --eval_frames 400  --initial_model baseline_v2_ap.model --train_path /var/data/db/FairVoice/FairVoice/FairVoice/Spanish --test_path /var/data/db/FairVoice/FairVoice/FairVoice/Spanish --train_list ./lists/Esp_List/Spanish_train.txt --test_list ./lists/Esp_List/Spanish_test_female.txt

python ./trainSpeakerNet.py --eval --model ResNetSE34L --log_input True --trainfunc angleproto --save_path exps/test --eval_frames 400 --initial_model baseline_lite_ap.model --train_path /var/data/db/FairVoice/FairVoice/FairVoice/Spanish --test_path /var/data/db/FairVoice/FairVoice/FairVoice/Spanish --train_list ./Esp_List/Spanish_train.txt --test_list ./Esp_List/Spanish_test_female.txt

---TESTEAR ENG---
python ./trainSpeakerNet.py --eval --model ResNetSE34V2 --log_input True --encoder_type ASP --n_mels 64 --trainfunc softmaxproto --save_path exps/test2 --eval_frames 400  --initial_model baseline_v2_ap.model --train_path /var/data/db/FairVoice/FairVoice/FairVoice/English --test_path /var/data/db/FairVoice/FairVoice/FairVoice/English --train_list ./Eng_List2/English_train.txt --test_list ./Eng_List2/English_test_male.txt

python ./trainSpeakerNet.py --eval --model ResNetSE34L --log_input True --trainfunc angleproto --save_path exps/test2 --eval_frames 400 --initial_model baseline_lite_ap.model --train_path /var/data/db/FairVoice/FairVoice/FairVoice/English --test_path /var/data/db/FairVoice/FairVoice/FairVoice/English --train_list ./Eng_List_Prueba/English_train.txt --test_list ./Eng_List_Prueba/English_test_young.txt



----------------------------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------------------------
------------------------------------FINE TUNING -----------------------------------------------------------

python ./FineTuning_blite2.py --model ResNetSE34V2 --log_input True --encoder_type ASP --n_mels 64 --trainfunc softmaxproto --save_path exp_pre/exp2001 --scale 30 --margin 0.3 --premodel baseline_v2_ap.model --train_path /var/data/db/FairVoice/FairVoice/FairVoice --test_path /var/data/db/FairVoice/FairVoice/FairVoice --train_list ./lists/EspPrueba/train_200_Esp.txt --test_list ./lists/EspPrueba/test_200_Esp.txt --newClases 200 --nPerSpeaker 2 

python ./FineTuning_blite.py --model ResNetSE34L --log_input True --trainfunc angleproto --save_path exp_pre/exp2001 --scale 30 --margin 0.3 --premodel baseline_lite_ap.model --train_path /var/data/db/FairVoice/FairVoice/FairVoice/English --test_path /var/data/db/FairVoice/FairVoice/FairVoice/English --train_list ./lists/Eng_List/train_1165_Eng.txt --test_list ./lists/Eng_List/test_1165_Eng.txt --newClases 200 --nPerSpeaker 2 


--TRAIN Pre model Lite Ingles
python ./FineTuning_bliteV2.py --model ResNetSE34L --log_input True --trainfunc angleproto --save_path exp_pre/exp2001 --scale 30 --margin 0.3 --premodel baseline_lite_ap.model --train_path /var/data/db/FairVoice/FairVoice/FairVoice/English --test_path /var/data/db/FairVoice/FairVoice/FairVoice/English --train_list ./lists/Eng_List/train_1165_Eng.txt --test_list ./lists/Eng_List/test_1165_Eng.txt --newClases 1165 --nPerSpeaker 2 

--TEST 
python ./trainSpeakerNet.py --eval --model ResNetSE34L --log_input True --trainfunc angleproto --save_path exp_pre/test2001 --eval_frames 400 --initial_model ./exp/esp486/train/model/model000000400.model --train_path /var/data/db/FairVoice/FairVoice/FairVoice/English --test_path /var/data/db/FairVoice/FairVoice/FairVoice/English --train_list ./lists/Eng_List/train_1165_Eng.txt --test_list ./lists/Eng_List/test_1165_Eng.txt --nOut 1165 


PRUEBA DE FUNCIONAMIENTO 

python ./FineTuning_bliteV2.py --model ResNetSE34L --log_input True --trainfunc angleproto --save_path exp_pre/exp2004 --scale 30 --margin 0.1 --premodel baseline_lite_ap.model --train_path /var/data/db/FairVoice/FairVoice/FairVoice --test_path /var/data/db/FairVoice/FairVoice/FairVoice --train_list ./lists/EspPrueba/train_200_Esp.txt --test_list ./lists/EspPrueba/test_200_Esp.txt --newClases 200 --nPerSpeaker 2  --lr 0.0001 --max_epoch 60

python ./trainSpeakerNet.py --eval --model ResNetSE34L --log_input True --trainfunc angleproto --save_path exp_pre/test2001 --eval_frames 400 --initial_model ./exp_pre/exp2004/model/model000000010.model --train_path /var/data/db/FairVoice/FairVoice/FairVoice --test_path /var/data/db/FairVoice/FairVoice/FairVoice --train_list ./lists/Esp_List/train_486_Esp.txt --test_list ./lists/Esp_List/female_486_Esp.txt --nOut 200 --encoder_type ASP



python ./trainSpeakerNet.py --eval --model ResNetSE34L --log_input True --trainfunc angleproto --save_path exp/esp486/test --eval_frames 400 --initial_model ./exp/esp486/train/model/model000000400.model --train_path /var/data/db/FairVoice/FairVoice/FairVoice/Spanish --test_path /var/data/db/FairVoice/FairVoice/FairVoice/Spanish --train_list ./Esp_List/Spanish_train.txt --test_list ./Esp_List/Spanish_test_male.txt  --nOut 486 --encoder_type SAP



-------TRAIN ESP
python ./FineTuning_bliteV2.py --model ResNetSE34L --log_input True --trainfunc angleproto --save_path exp/esp486/train --scale 30 --margin 0.1 --premodel baseline_lite_ap.model --train_path /var/data/db/FairVoice/FairVoice/FairVoice/Spanish --test_path /var/data/db/FairVoice/FairVoice/FairVoice/Spanish --train_list ./lists/Esp_List/train_486_Esp.txt --test_list ./lists/Esp_List/test_486_Esp.txt --newClases 486 --nPerSpeaker 2  --lr 0.0001 --max_epoch 400 --batch_size 80


python ./trainSpeakerNet.py --eval --model ResNetSE34L --log_input True --trainfunc angleproto --save_path exp/esp486/test --eval_frames 400 --initial_model ./exp/esp486/train/model/model000000400.model --train_path /var/data/db/FairVoice/FairVoice/FairVoice/Spanish --test_path /var/data/db/FairVoice/FairVoice/FairVoice/Spanish --train_list ./Esp_List/Spanish_train.txt --test_list ./Esp_List/Spanish_test_male.txt  --nOut 486 --encoder_type SAP


python ./trainSpeakerNet.py --eval --model ResNetSE34V2 --log_input True --encoder_type ASP --n_mels 64 --trainfunc softmaxproto --save_path exp/esp486/test --eval_frames 400 --initial_model baseline_lite_ap.model --train_path /var/data/db/FairVoice/FairVoice/FairVoice/Spanish --test_path /var/data/db/FairVoice/FairVoice/FairVoice/Spanish --train_list ./Esp_List/Spanish_train.txt --test_list ./Esp_List/Spanish_test_female.txt 


python ./trainSpeakerNet.py --eval --model ResNetSE34L --log_input True --trainfunc angleproto --encoder_type ASP --save_path exp/esp486/test --eval_frames 400 --initial_model baseline_lite_ap.model --train_path /var/data/db/FairVoice/FairVoice/FairVoice/Spanish --test_path /var/data/db/FairVoice/FairVoice/FairVoice/Spanish --train_list ./Eps_List2/Spanish_train.txt --test_list ./Eps_List/Spanish_test_male.txt 


-------TRAIN ENG
python ./FineTuning_bliteV2.py --model ResNetSE34L --log_input True --trainfunc angleproto --save_path exp/eng1165/train --scale 30 --margin 0.1 --premodel baseline_lite_ap.model --train_path /var/data/db/FairVoice/FairVoice/FairVoice/English --test_path /var/data/db/FairVoice/FairVoice/FairVoice/English --train_list ./lists/Eng_List/train_1165_Eng.txt --test_list ./lists/Eng_List/test_1165_Eng.txt --newClases 1165 --nPerSpeaker 2  --lr 0.001 --max_epoch 400 --batch_size 200


python ./trainSpeakerNet.py --eval --model ResNetSE34L --log_input True --trainfunc angleproto --save_path exp/esp486/test --eval_frames 400 --initial_model ./exp/esp486/train/model/model000000400.model --train_path /var/data/db/FairVoice/FairVoice/FairVoice/Spanish --test_path /var/data/db/FairVoice/FairVoice/FairVoice/Spanish --train_list ./lists/train_486_Spanish.txt --test_list ./lists/Eps_List2/_Spanish.txt --nOut 486 --enconder_type ASP