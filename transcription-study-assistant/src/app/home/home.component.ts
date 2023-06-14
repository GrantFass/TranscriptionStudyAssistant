import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { UploadLecturesComponent } from '../upload-lectures/upload-lectures.component';
import { EditorComponent } from '../editor/editor.component';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  constructor(
    private router:Router
  ){}

  ngOnInit(): void {
    
  }

  uploadButton(){
    console.log("reaching upload lecture");
    this.router.navigate(['./upload-lectures']);
  }

  editorButton(){
    console.log("reaching editor");
    this.router.navigate(['./editor']);
  }

  summariesButton(){
    console.log("reaching summaries");
    this.router.navigate(['./summaries']);
  }

  studyMaterialsButton(){
    console.log("reaching study materials");
    this.router.navigate(['./study-materials']);
  }
}

