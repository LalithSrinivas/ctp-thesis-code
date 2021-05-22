import argparse
import pandas as pd
import counter
import sys
import numpy as np

if __name__ == '__main__':
    argparser = argparse.ArgumentParser('Sampler', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    argparser.add_argument('--mode', choices=['random', 'top', 'bottom'], action='store', type=str, default='random')
    argparser.add_argument('--counter-file', action='store', type=str, default='sub_obj.csv')
    argparser.add_argument('--num-entities', action='store', type=int, default='10')
    argparser.add_argument('--input-directory', action='store', type=str, default='../yago_files/')
    argparser.add_argument('--output-directory', action='store', type=str, default='../yago_sampled_files/')

    args = argparser.parse_args(sys.argv[1:])
    top_entities = pd.read_csv(args.counter_file, header=None)
    if args.mode == 'top':
        top_entities = list(top_entities.head(args.num_entities)[0])
    elif args.mode == 'bottom':
        top_entities = list(top_entities.tail(args.num_entities)[0])
    else:
        top_entities = list(top_entities.sample(n=args.num_entities)[0])
    # print(top_entities)
    train_df = pd.read_csv(args.input_directory+'/train.tsv', sep='\t', names=['s', 'p', 'o'], dtype={'s':str, 'p':str, 'o':str})
    test_df = pd.read_csv(args.input_directory+'/test.tsv', sep='\t', names=['s', 'p', 'o'], dtype={'s':str, 'p':str, 'o':str})
    dev_df = pd.read_csv(args.input_directory+'/dev.tsv', sep='\t', names=['s', 'p', 'o'], dtype={'s':str, 'p':str, 'o':str})

    train_df = train_df.loc[(train_df['s'].isin(top_entities) | train_df['o'].isin(top_entities))]
    print(len(train_df))
    test_df = test_df.loc[test_df['s'].isin(top_entities) | test_df['o'].isin(top_entities)]
    dev_df = dev_df.loc[dev_df['s'].isin(top_entities) | dev_df['o'].isin(top_entities)]
    train_df.to_csv(args.output_directory+'/train.tsv', sep='\t', header=False)
    test_df.to_csv(args.output_directory+'/test.tsv', sep='\t', header=False)
    dev_df.to_csv(args.output_directory+'/dev.tsv', sep='\t', header=False)
