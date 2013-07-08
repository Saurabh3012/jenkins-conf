'''
  @file kmeans.py
  @author Marcus Edel

  K-Means Clustering with mlpy.
'''

import os
import sys
import inspect

# Import the util path, this method even works if the path contains symlinks to
# modules.
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(
  os.path.split(inspect.getfile(inspect.currentframe()))[0], "../../util")))
if cmd_subfolder not in sys.path:
  sys.path.insert(0, cmd_subfolder)

from log import *
from timer import *

import numpy as np
import mlpy

'''
This class implements the K-Means Clustering benchmark.
'''
class KMEANS(object):

  ''' 
  Create the K-Means Clustering benchmark instance.
  
  @param dataset - Input dataset to perform K-Means on.
  @param verbose - Display informational messages.
  '''
  def __init__(self, dataset, verbose=True): 
    self.verbose = verbose
    self.dataset = dataset

  '''
  Destructor to clean up at the end.
  '''
  def __del__(self):
    pass

  '''
  Use the mlpy libary to implement K-Means Clustering.

  @param options - Extra options for the method.
  @return - Elapsed time in seconds or -1 if the method was not successful.
  '''
  def KMeansMlpy(self, options):
    totalTimer = Timer()

    # Load input dataset.
    Log.Info("Loading dataset", self.verbose)
    data = np.genfromtxt(self.dataset, delimiter=',')

    # Gather parameters.
    clusters = re.search('-c (\d+)', options)
    seed = re.search("-s (\d+)", options)

    # Now do validation of options.
    if not clusters:
      Log.Fatal("Required option: Number of clusters or cluster locations.")
      return -1
    elif clusters.group(1) < 1:
      Log.Fatal("Invalid number of clusters requested! Must be greater than or "
          + "equal to 1.")
      return -1

    with totalTimer:
      # Create the KMeans object and perform K-Means clustering.
      if seed:
        kmeans = mlpy.kmeans(data, int(clusters.group(1)), seed=int(seed.group(1)))
      else:
        kmeans = mlpy.kmeans(data, int(clusters.group(1)))

    return totalTimer.ElapsedTime()

  '''
  Perform K-Means Clustering. If the method has been successfully completed 
  return the elapsed time in seconds.

  @param options - Extra options for the method.
  @return - Elapsed time in seconds or -1 if the method was not successful.
  '''
  def RunMethod(self, options):
    Log.Info("Perform K-Means.", self.verbose)

    return self.KMeansMlpy(options)
