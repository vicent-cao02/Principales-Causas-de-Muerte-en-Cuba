import streamlit as st
import streamlit_analytics 
import json
import matplotlib.pyplot as plt

streamlit_analytics.track(save_to_json = "./data/metrics.json" ) 
streamlit_analytics.track(load_from_json="./data/metrics.json")