# Commands used to achieving results shown in thesis document.

## Init

- Thesis report can be found [here](https://github.com/LalithSrinivas/btp_thesis)
- Freebase dataset files were located at /home/baadalvm/data/fb15k-237 directory. The directory has train, test, dev data files in CSV format.
- We have used ```free -mh``` to observe the memory utilized by a model.
- We have added a few print statements in the code to observe time taken for to run that segment of code.
- We have used *profilehooks* to identify bottlenecks.

## Original CTP Execution

```
./bin/hoppy-cli.py --train /home/baadalvm/data/fb15k-237/train.csv 
                   --test /home/baadalvm/data/fb15k-237/test.csv 
                   --dev /home/baadalvm/data/fb15k-237/valid.csv 
                   -e 5 -b 500 --seed 1 --eval-batch-size 500 
                   --refresh-interval 100 -k 100
```

## CTP+TransE model Execution

- CTP model is used for the Training and Scoring. TransE model is used for performing KNN search.
- **--top-k** is the argument used for varying the value of K in KNN search. The commands are as follows.
  - K = 10
    ```
    ./bin/hoppy-transe-cli.py --train /home/baadalvm/data/fb15k-237/train.csv 
                              --test /home/baadalvm/data/fb15k-237/test.csv 
                              --dev /home/baadalvm/data/fb15k-237/valid.csv 
                              -e 20 -b 500 --seed 1 --eval-batch-size 500 
                              --refresh-interval 100 --save fb-hoppy-transe-params-10.txt 
                              -k 100 --top-k 10 --transe-eval --load-transe fb-transe-params.txt
    ```
  - K = 25
    ```
    ./bin/hoppy-transe-cli.py --train /home/baadalvm/data/fb15k-237/train.csv 
                              --test /home/baadalvm/data/fb15k-237/test.csv 
                              --dev /home/baadalvm/data/fb15k-237/valid.csv 
                              -e 20 -b 500 --seed 1 --eval-batch-size 500 
                              --refresh-interval 100 --save fb-hoppy-transe-params-25.txt 
                              -k 100 --top-k 25 --transe-eval --load-transe fb-transe-params.txt
    ```
  - K = 50
    ```
    ./bin/hoppy-transe-cli.py --train /home/baadalvm/data/fb15k-237/train.csv 
                              --test /home/baadalvm/data/fb15k-237/test.csv 
                              --dev /home/baadalvm/data/fb15k-237/valid.csv 
                              -e 20 -b 500 --seed 1 --eval-batch-size 500 
                              --refresh-interval 100 --save fb-hoppy-transe-params-50.txt 
                              -k 100 --top-k 50 --transe-eval --load-transe fb-transe-params.txt
    ```
  - K = 100
    ```
    ./bin/hoppy-transe-cli.py --train /home/baadalvm/data/fb15k-237/train.csv 
                              --test /home/baadalvm/data/fb15k-237/test.csv 
                              --dev /home/baadalvm/data/fb15k-237/valid.csv 
                              -e 20 -b 500 --seed 1 --eval-batch-size 500 
                              --refresh-interval 100 --save fb-hoppy-transe-params-100.txt 
                              -k 100 --top-k 100 --transe-eval --load-transe fb-transe-params.txt
    ```

- The TransE evaluation will happen only when the **--transe-eval** argument is provided, else the normal evaluation will take place.
- The KNN search is performed over TransE embedding space as mentioned before. For this, we have to train the TransE model and store the embeddings.
- As you can see in the above commands, the saved TransE embeddings are saved using the argument **--load-transe**.

## Training, Saving TransE

- As mentioned in the above sigment, to execute CTP with TransE evaluation, we must train and save TransE model first. The following command was used for training and saving the TransE model.

```
./bin/transe-cli.py --train /home/baadalvm/data/fb15k-237/train.csv 
                    --test /home/baadalvm/data/fb15k-237/test.csv 
                    --dev /home/baadalvm/data/fb15k-237/valid.csv 
                    -e 20 -b 1000 --seed 1 --eval-batch-size 1000 
                    --save fb-transe-params.txt --model transe
```

- The *"--model"*, *"--save"* arguments take care of choosing the training model and saving location respectively.
