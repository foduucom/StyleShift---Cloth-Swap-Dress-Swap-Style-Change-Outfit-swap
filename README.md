---
language:
- en
tags:
- ClothSwap
- TryOn
- StyleChange
- DressChange
- ClothShift
- TryCloth
- FashionNew
- SwapCloth
- DressSwap
- OutfitSwap
license: apache-2.0
---
##  StyleShift - Cloth Swap / Dress Swap / Style Change / Outfit Swap

This project showcases a Cloth Swap feature, leveraging the powerful capabilities of ComfyUI, a modular and flexible interface for AI workflows. This guide provides step-by-step instructions to set up, use, and contribute to the project.

<div align="center">
  <img width="600" height="500" alt="foduucom/ClothSwap" src="https://huggingface.co/foduucom/StyleShift-ClothSwap/resolve/main/output.png">
</div>

## Objective

The primary objective is to provide a simple, effective, and customizable tool for tasks such as virtual try-ons, creative prototyping, and realistic clothing mockups. Whether you're an e-commerce platform, a fashion designer, or just experimenting with image manipulation, this project offers endless possibilities.

## Clone and Setup ComfyUI Repository

Install ComfyUI by cloning its main repository:

```bash
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI
```
Install dependencies:

```bash
pip install -r requirements.txt
```

Install ComfyUI Manager:

go to ComfyUI/custom_nodes dir in terminal(cmd) and clone this repo:

```bash
git clone https://github.com/ltdrdata/ComfyUI-Manager.git
```
<b>Restart ComfyUI</b>

To Start ComfyUI:

```bash
python3 main.py
```
Note: ComfyUI requires Python 3.9 or above. Ensure all required dependencies are installed.

Now Go to Manager ->-> Custom Nodes Manager and install this two nodes <b>ComfyUI Layer Style</b> and <b>ComfyUI_CatVTON_Wrapper</b>, restart and reload the page.

<div align="center">
  <img width="800" height="800" alt="foduucom/ClothSwap" src="https://huggingface.co/foduucom/ClothSwap/resolve/main/custom_nodes.png">
</div>

Place the <b>sam_vit_h_4b8939.pth</b> model inside ComfyUI/models/sams directory and <b>groundingdino_swint_ogc.pth</b> model in ComfyUI/models/grounding-dino directory if not download it.
(If directory name not there in ComfyUI/models/ create new)

- For Reference you can download model by below link:
https://huggingface.co/ShilongLiu/GroundingDINO/resolve/main/groundingdino_swint_ogc.pth
https://huggingface.co/spaces/abhishek/StableSAM/resolve/main/sam_vit_h_4b8939.pth

## Clone this Repository
Clone the repository containing the Cloth Swap JSON workflows and assets:

```bash
git clone https://huggingface.co/foduucom/StyleShift-ClothSwap
cd StyleShift-ClothSwap
```

## How to use

- Start <b>ComfyUI</b> (by running python3 main.py)
- Open ComfyUI in your browser (default: http://127.0.0.1:8188)
- Click on <b>Load</b> button in menu bar and select the <b>workflow.json</b> file provided in this repository
- Now click on <b>Queue Prompt</b> for generate output

or you can use by python script provided in this repository:
```bash 
python3 main.py

#Remember change the input paths in script here :
#prompt["2"]["inputs"]["image"] = "\\ put your input person pose image"
#prompt["3"]["inputs"]["image"] = "\\ put your input cloth image"
```

## Using Cloth Swap

- Prepare your input images (ensure proper resolution for better results)
- Select the uploaded workflow in ComfyUI
- Provide necessary inputs as per the workflow:
  - Source Image: The base image where the clothing is to be swapped
  - Cloth Image: The image of the clothing to be applied
- Start the process to generate swapped outputs
- Save the generated images for further use

## Why is this Useful?
This project has a broad range of applications, making it useful across multiple industries and for personal use:

- <b/>Virtual Try-On Technology:</b>
Revolutionize online shopping experiences by enabling customers to "try on" clothes digitally.
Reduce product returns by providing a realistic preview of clothing fit and style.

- <b>Fashion Design and Prototyping:</b>
Help designers test their creations on various models without the need for physical samples or photoshoots.
Quickly iterate designs and visualize the final product.

## Compute Infrastructure

## Hardware

NVIDIA GeForce RTX 3060 card

## Model Card Contact

For inquiries and contributions, please contact us at info@foduu.com.

```bibtex
@ModelCard{
  author    = {Nehul Agrawal and
               Priyal Mehta},
  title     = {StyleShift - Cloth Swap / Dress Swap / Style Change},
  year      = {2024}
}
```
